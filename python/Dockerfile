FROM sagemath/sagemath:latest

RUN sage --pip install grpcio googleapis-common-protos

COPY . clt

CMD ["PYTHONPATH=clt sage clt/examples/extremal_rays.py"]
#CMD ["bash"]