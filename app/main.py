from chirpstack_api_wrapper import *
import argparse
import time
import logging

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

    #Create client
    client = ChirpstackClient(args.chirpstack_account_email,args.chirpstack_account_password,args.chirpstack_api_interface,False)
    n = 10
    while not client.ping():
        if n > 300:
            logging.error("retry limit exceeded")
            sys.exit(1) # Exit with a non-zero status code to indicate failure
        print(f"Retrying in {n} seconds...")
        time.sleep(n)
        n*=2

    #Gateway record
    gw = Gateway(name="wes-gateway", gateway_id="D2CE19FFFEC9D449", tenant_id="52f14cd4-c6f1-4fbd-8f87-4025e1d49242")

    #if not found, create
    if not client.get_gateway(gw): 
        client.create_gateway(gw)
    return

if __name__ == "__main__":
    main() 