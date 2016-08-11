FROM kaixhin/torch:latest
MAINTAINER Sang Han jjangsangy@gmail.com

RUN sudo apt-get -y update && sudo apt-get -y upgrade \
    && sudo apt-get -y install libprotobuf-dev protobuf-compiler libhdf5-serial-dev hdf5-tools \
    && luarocks install nn \
    && luarocks install nngraph \
    && luarocks install image \
    && luarocks install loadcaffe \
    && git clone https://github.com/mpx/lua-cjson /tmp/cjson && cd /tmp/cjson && luarocks make \
    && git clone https://github.com/deepmind/torch-hdf5.git /tmp/torch-hdf5 && cd /tmp/torch-hdf5 luarocks make \
    && rm -rf /tmp/*
