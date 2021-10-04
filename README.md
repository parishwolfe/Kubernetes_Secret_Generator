# Kubernetes Secrets YAML Generator

# arguments

- name = name of the secret
- namespace = optional, include namespace in metadata
- csv = csv with secrets, headers of key,value

# usage

`python3 kubesecret.py --name test --namespace default --csv test.csv`  
