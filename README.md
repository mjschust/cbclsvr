To run the server:

bash: docker run -ti --rm -p 50051:50051 mjschust/cbsvr:test

To run the client:

bash: docker run -ti --rm --network="host" mjschust/cbclt:test