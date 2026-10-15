#nullable enable
using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;

// Test-only in-memory stream. No files, network, child process or live input.
public sealed class Dsp004BoundedReadSyntheticFixtureRev1 : Stream
{
    private readonly byte[] data;
    private readonly int chunk, failCall, cancelCall, earlyEndCall;
    private int position;
    public int ReadCalls { get; private set; }
    public int ReturnedBytes => position;
    public int MaximumRequested { get; private set; }
    public bool ZeroReturned { get; private set; }
    public bool WasDisposed { get; private set; }
    public IOException? HeldFailure { get; }

    public Dsp004BoundedReadSyntheticFixtureRev1(byte[] input, int maximumChunk, int failOnCall, int cancelOnCall, int earlyEofOnCall)
    {
        if (input == null || maximumChunk < 1) throw new ArgumentException("SYNTHETIC_FIXTURE_ARGUMENT");
        data = (byte[])input.Clone();
        chunk = maximumChunk; failCall = failOnCall; cancelCall = cancelOnCall; earlyEndCall = earlyEofOnCall;
        if (failCall > 0) HeldFailure = new IOException("SYNTHETIC_READ_FAILURE");
    }

    public static byte[] CreateData(int length)
    {
        if (length < 0 || length > 262145) throw new ArgumentOutOfRangeException(nameof(length));
        var result = new byte[length];
        for (int i = 0; i < result.Length; i++) result[i] = (byte)(i % 251);
        return result;
    }

    public override ValueTask<int> ReadAsync(Memory<byte> buffer, CancellationToken cancellationToken = default)
    {
        if (WasDisposed) throw new ObjectDisposedException(nameof(Dsp004BoundedReadSyntheticFixtureRev1));
        ReadCalls++;
        MaximumRequested = Math.Max(MaximumRequested, buffer.Length);
        if (ReadCalls == failCall) return new ValueTask<int>(Task.FromException<int>(HeldFailure!));
        if (ReadCalls == cancelCall) return new ValueTask<int>(Task.FromCanceled<int>(new CancellationToken(true)));
        if (ReadCalls == earlyEndCall || position == data.Length)
        {
            ZeroReturned = true;
            return new ValueTask<int>(0);
        }
        int count = Math.Min(buffer.Length, Math.Min(chunk, data.Length - position));
        data.AsMemory(position, count).CopyTo(buffer);
        position += count;
        return new ValueTask<int>(count);
    }

    public override bool CanRead => !WasDisposed;
    public override bool CanSeek => false;
    public override bool CanWrite => false;
    public override long Length => data.Length;
    public override long Position { get => position; set => throw new NotSupportedException(); }
    public override int Read(byte[] buffer, int offset, int count) => throw new NotSupportedException("ASYNC_MEMORY_READ_ONLY");
    public override void Flush() { }
    public override long Seek(long offset, SeekOrigin origin) => throw new NotSupportedException();
    public override void SetLength(long value) => throw new NotSupportedException();
    public override void Write(byte[] buffer, int offset, int count) => throw new NotSupportedException();
    protected override void Dispose(bool disposing) { WasDisposed = true; base.Dispose(disposing); }
}
