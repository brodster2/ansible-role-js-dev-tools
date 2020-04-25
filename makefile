.PHONY: all

test:
	docker run --rm -it \
    -v $(basename "${PWD}"):/tmp/$(basename "${PWD}"):ro \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -w /tmp/$(basename "${PWD}") \
    quay.io/ansible/molecule:latest \
    sudo molecule test