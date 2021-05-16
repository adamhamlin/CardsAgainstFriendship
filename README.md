# Cards Against Friendship
No frills, containerized Cards Against Humanity clone with custom card additions. Play with your friends on a private server hosted from your computer!

This relies on https://github.com/emcniece/DockerYourXyzzy, which is the dockerized version of PretendYourXyzzy.

## Prerequisites
You will need the following programs in order to run:
- [docker](https://docs.docker.com/get-docker)
- [sqlite3](https://sqlite.org/download.html) (Recommend the pre-compiled binaries)
- [ngrok](https://dashboard.ngrok.com/get-started/setup)

## Add Custom Cards
To add custom cards, you should update the 2 tsv files in the `custom-cards` directory. Follow the examples already there, but note that `black-cards.tsv` is in the format `<DRAW_COUNT>\t<PICK_COUNT>\t<CARD_TEXT>`, where `DRAW_COUNT` is how many cards should be drawn (usually 0) and `PICK_COUNT` is how many cards should be played (usually equals the number of blanks in the `CARD_TEXT`). Thus, a standard "Pick 2" would have a draw count of 1 and a pick count of 2.

>NOTE: This only needs to be run once, but it should be run again if you modify your custom card lists.
```bash
./add-custom-cards.sh "<My Custom Deck Name>" "<Watermark Text>"
```

## Run it!
```bash
docker run -d -p 8080:8080 --name cah -v ${PWD}/pyx.sqlite:/project/pyx.sqlite emcniece/dockeryourxyzzy:latest
```

## Play with your friends!
Run below command to get a publicly available URL for your local webserver:
```bash
ngrok http 8080
```