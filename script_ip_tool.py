import argparse

"""
Note: host order!
3.0.168.192
"""

def encode(args):
    ip_parts = [int(i) for i in args.ip.split('.')]
    assert len(ip_parts) == 4, "invalid ip given"
    print((ip_parts[0] << 24) + (ip_parts[1] << 16) + (ip_parts[2] << 8) + ip_parts[3])

def encode_host(args):
    ip_parts = [int(i) for i in args.ip.split('.')]
    assert len(ip_parts) == 4, "invalid ip given"
    print((ip_parts[3] << 24) + (ip_parts[2] << 16) + (ip_parts[1] << 8) + ip_parts[0])

def decode(args):
    ident = args.id
    parts = [
        str((ident & 0xff000000) >> 24),
        str((ident & 0xff0000) >> 16),
        str((ident & 0xff00) >> 8),
        str((ident & 0xff))
    ]
    print('.'.join(parts))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='IP Encode',
                    description='Encode/decodes ips to unint')

    subparser = parser.add_subparsers()
    encode_parser = subparser.add_parser("encode")
    encode_parser.add_argument("ip", type=str, help="IP address string to encode")
    encode_parser.set_defaults(func=encode)

    encode_host_parser = subparser.add_parser("encode_host")
    encode_host_parser.add_argument("ip", type=str, help="IP address string to encode (in host order)")
    encode_host_parser.set_defaults(func=encode_host)

    decode_parser = subparser.add_parser("decode")
    decode_parser.add_argument("id", type=int, help="uint version of the ip")
    decode_parser.set_defaults(func=decode)

    args = parser.parse_args()
    args.func(args)


