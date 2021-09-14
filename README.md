# tn3-edges
- Create guest account
- Backup current config

## Usage of this playbook
Shallow clone this repository and setup ansible.
```
% git clone --depth 1 https://github.com/yamaoka-kitaguchi-lab/tn3-edges
% cd tn3-edges
% pipenv update
% pipenv run install
```

Edit targets and check their statuses with:
```
% vim inventories/production/edges
% deadman inventories/production/edges
```

Edit the name and password of newly creating guest by:
```
% vim inventories/production/group_vars/guest_account.yml
```

### Create guest account
Create read-only account on all edges with given password by:
```
% pipenv run addguest
```

### Backup current config
Backup current config by:
```
% pipenv run backup
```
