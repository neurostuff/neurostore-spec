# neurostore-spec

Somewhat misnamed, this repo contains the openAPI specifications for both neurostore and neurosynth-compose.

The openAPI specs are based on the [NIMADS specification](https://github.com/neurostuff/NIMADS), and any changes to NIMADS is pushed to the
neurostore/neurosynth-compose openAPI specification based on a github action flow.

Subsequently, changes to the neurostore/neurosynth-compose openAPI specification update their respective typescript and python SDKs
through a similar github action.

Thus any new branches/changes made to NIMADs or the openAPI specifications will result in an update to the python/typescript SDKs.

