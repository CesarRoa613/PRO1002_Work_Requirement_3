# PRO1002 – Work Requirement 3

A small Python script that resolves a hostname to an IPv4 address and prints a greeting with the result.

## Requirements

- Python 3
- No external packages are required.

## How to run

Open a terminal in the project folder and run:

```powershell
py hostname_lookup.py
```

On systems where Python is started with `python3`, use:

```bash
python3 hostname_lookup.py
```

## Expected output

```text
Hello! The IP address of localhost is 127.0.0.1.
```

The script uses `socket.gethostbyname()` to resolve `localhost`.
It performs a hostname lookup without establishing a client-server connection.

## Reflection

Module 5 introduced how browsers and web servers communicate through HTTP requests and responses. IP handles addressing and routing, while TCP provides reliable, ordered data delivery. The socket API gives programs access to networking functions. In this task, I used Python's socket module to resolve localhost to an IPv4 address and print a greeting. A challenging concept is distinguishing hostname resolution from establishing a connection: finding an address does not mean a connection has been made. I want to explore how a client connects to a server and exchanges data, turning these networking concepts into a practical example.

## License

This project is licensed under the MIT License. See LICENSE for details.