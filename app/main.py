from chirpstack_api_wrapper import *
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--chirpstack-account-email",
        default=os.getenv("CHIRPSTACK_ACCOUNT_EMAIL"),
        help="The Chirpstack Account's email to use to access APIs",
    )
    parser.add_argument(
        "--chirpstack-account-password",
        default=os.getenv("CHIRPSTACK_ACCOUNT_PASSWORD"),
        help="The Chirpstack Account's password to use to access APIs",
    )
    parser.add_argument(
        "--chirpstack-api-interface",
        default=os.getenv("CHIRPSTACK_API_INTERFACE"),
        help="Chirpstack's server API interface. The port is usually 8080",
    )
    args = parser.parse_args()

    client = ChirpstackClient(args.chirpstack_account_email,args.chirpstack_account_password,args.chirpstack_api_interface)

    gw = Gateway(name="wes-gateway", gateway_id="D2CE19FFFEC9D449", tenant_id="52f14cd4-c6f1-4fbd-8f87-4025e1d49242")

    client.create_gateway(gw)

if __name__ == "__main__":
    main() 