# Strings and Byte Strings

The only thing that a computer can store is bytes. To store anything in a computer, you must first `encode` it, i.e. convert it to bytes. For example,

- If you want to store music, you must first encode it using `MP3`, `WAV`, etc.
- If you want to store a picture, you must first encode it using `PNG`, `JPEG`, etc.
- If you want to store text, you must first encode it using `ASCII`, `UTF-8`, etc.

`MP3`, `WAV`, `PNG`, `JPEG`, `ASCII` and `UTF-8` are examples of encoding. An encoding is a format to represent audio, images, text, etc in bytes. In Python, a byte string is just that, a sequence of bytes, **it is not human-readable**. Under the hood, everything must be converted to a byte string before it can be stored in a computer.

On the other hand, a character string, often just called a "string" is a sequence of characters. It is human readable. A character string can't be directly stored in a computer, it has to be encoded first (converted to a byte string). There are multiple encodings through which a character string can be converted into a byte string, such as `ASCII` and `UTF-8`. When we talk about encoding a string as a byte string, it means converting the string into a sequence of 1s and 0s, specifically binary data, where each unit of data is represented by a byte (8 bits).

For example, let's consider the string "Hello" encoded in `UTF-8`. The `UTF-8` encoding scheme represents characters using variable-length byte sequences. When we encode "Hello" in `UTF-8`, it would be represented as a byte string consisting of the following bytes:

```
01001000 01100101 01101100 01101100 01101111
```

In this binary representation, each sequence of 8 bits (1 byte) corresponds to a character in the string. The bytes can be stored, transmitted, or processed as binary data.

# Code Examples

```Python
'I am a string'.encode('ASCII')
'I am a string'.encode('UTF-8')
```

The above Python code will encode the string `I am a string` using the encoding `ASCII` and `UTF-8`. The result of the above code all be a byte string. If you print it, Python will represent it as `b'I am a string'`. Remember, however, that byte strings **aren't human readable**. What is happening here is that Python is decoding them from `ASCII` when you print them. In Python, a byte string is represented by a `b`, followed by the byte strings `ASCII` representation.

For example, if I encode something that is not `ASCII` or `UTF-8`, it will not print the original characters.

```Python
print('I am a string'.encode('UTF-16'))
```

Will give us,

```
b'\xff\xfeI\x00 \x00a\x00m\x00 \x00a\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00'
```

However, correctly knowing the encoding scheme, it can be correctly decoded.

```Python
b'I am a string'.decode('ASCII')
```

Will output,

```
'I am a string'
```

However, notice here, that the prefix `b` is missing. This is **not a byte string**. Encoding and decoding are inverse operations. Everything must be encoded before it can be written to disk, and it must be decoded before it can be read by a human. When a string is encoded, its characters are mapped to the corresponding binary representations according to the chosen encoding scheme. This encoded representation can be stored in a file, transmitted over a network, or used for various other purposes. To make use of the encoded string, it needs to be decoded, which involves reversing the process and converting the binary data back into its original character representation.