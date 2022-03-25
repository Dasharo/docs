# Dump with fwdump-docker

1. Get docker engine on DUT.
[Link to instructions](https://docs.docker.com/engine/install/ubuntu/).

2. Get fwdump-docker image:

    ```bash
    sudo docker pull 3mdeb/fwdump-docker:1.2.0
    ```

3. Use docker to get dump:

    ```bash
    docker run --rm --privileged -it -v $PWD:/home/fwdump 3mdeb/fwdump-docker:1.2.0 getlogs
    ```
