FROM gcc:4.9
COPY . /usr/src/work
WORKDIR /usr/src/work
RUN make
ENTRYPOINT ["./run_all.py"]
