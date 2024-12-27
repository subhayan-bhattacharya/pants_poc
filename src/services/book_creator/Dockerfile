FROM harbor.elevait.io/elevait/python-deployment-base:v3.12 AS build

ARG PIP_INDEX_URL
ARG PIP_DEFAULT_TIMEOUT=100

ENV PIP_INDEX_URL=$PIP_INDEX_URL
ENV PIP_DEFAULT_TIMEOUT=$PIP_DEFAULT_TIMEOUT

COPY --chown=1000 . .

ARG BUILDKIT_CACHE_PREFIX="pants_poc"

RUN --mount=type=cache,sharing=locked,id=${BUILDKIT_CACHE_PREFIX}-pip-cache,target=~/.cache/pip \
    --mount=type=bind,source=.git,target=.git                                                   \
    pip install --target /service/site-packages .[service] --constraint requirements.txt

# We use multi-stage build here, see: https://docs.docker.com/build/building/multi-stage/
# Everything that is added before this comment will not have any affect on the resulting docker image.
# Therefore please add your customizations just after this FROM layer.
FROM harbor.elevait.io/elevait/python-deployment-base:v3.12

# TARGET_DIR comes from python-deployment-base.
# https://bitbucket.org/elevait/python-deployment-base/src/main/Dockerfile
COPY --from=build /service/site-packages ${TARGET_DIR}

COPY src/services/utils ${TARGET_DIR}/utils

COPY src/services/book_creator .

ENTRYPOINT ["python", "app.py"]