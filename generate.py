from certificate import gen_root_ca, gen_ca, gen_service, load_key, load_cert, verify_cert
import argparse

DEFAULT_FILENAME = {
    "root": "root_ca",
    "ca": "intermedia_ca",
    "domain": "default.example.com",
}
DEFAULT_COMMON_NAME = {
    "root": "Local Root CA",
    "ca": "Local Intermediate CA",
    "domain": "default.example.com",
}

def main():
    # verify_cert()

    parser = argparse.ArgumentParser(description='Certificate Authority Service')
    parser.add_argument('mode', choices=['root', 'ca', 'domain'], default='domain')
    parser.add_argument('--name', type=str, required=False)
    parser.add_argument('--output', type=str, required=False)

    args = parser.parse_args()
    common_name = args.name if args.name else DEFAULT_COMMON_NAME[args.mode]
    filename = args.output if args.output else DEFAULT_FILENAME[args.mode]
    print("Generating %s: %s into %s.crt, %s.key" %(args.mode, common_name, filename, filename))

    if args.mode == 'root':
        gen_root_ca(common_name=common_name, filename=filename)
    elif args.mode == 'ca':
        root_private_key = load_key("certs/root_ca.key")
        root_cert = load_cert("certs/root_ca.crt")
        gen_ca(
            root_cert=root_cert,
            root_private_key=root_private_key,
            common_name=common_name,
            filename=filename
        )
    elif args.mode == 'domain':
        domain = common_name
        ca_private_key = load_key("certs/intermediate_ca.key")
        ca_cert = load_cert("certs/intermediate_ca.crt")
        gen_service(
            ca_cert=ca_cert,
            ca_private_key=ca_private_key,
            domain=domain
        )

main()
