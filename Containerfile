FROM debian:bookworm-slim

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
       ca-certificates \
       make \
       pandoc \
       python3 \
       texlive-fonts-recommended \
       texlive-latex-extra \
       texlive-xetex \
       zip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work
COPY . /work

CMD ["make", "pdf"]
