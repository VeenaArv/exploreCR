import os
import clashroyale
import logging

logger = logging.getLogger('clashroyale')
token = os.getenv('cr_api')

def main():
    client = clashroyale.RoyaleAPI(token=token)
    profile = client.get_player('#LRURQG0CR')  # library cleans the tag (strips #)
    logger.info(repr(profile))

if __name__ == '__main__':
    main()
