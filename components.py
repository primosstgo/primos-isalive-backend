#from docker import Container?

def get_container_data(container):
    container.reload()
    data = {
        'id': container.id,
        'status': container.status,
        'name': container.name,
        'creation_time': container.attrs['Created'],
        'ports': set(),
        # 'labels': container.labels,
        # 'exit_code': container.attrs['State']['ExitCode'],
    }
    for ips in container.ports.values():
        for ip in ips:
            if ip['HostIp'] in ('0.0.0.0', '::'):
                data['ports'].add(int(ip['HostPort']))
    data['ports'] = sorted(data['ports'])
    if data['status'] == 'running':
        data['status_time'] = container.attrs['State']['StartedAt']
    elif data['status'] == 'exited':
        data['status_time'] = container.attrs['State']['FinishedAt']
    else:
        data['status_time'] = None
    return data

def getContainerById(id: str):
    client = docker.from_env()
    container = client.containers.get(id)
    return {
        'id': container.id,
        'name': container.name,
        'image': container.attrs['Config']['Image'],
        'status': container.status,
        'created_at': container.attrs['Created'],
        'ports': container.attrs['HostConfig']['PortBindings'],
        'labels': container.labels,
        'exit_code': container.attrs['State']['ExitCode'],
        'exit_time': container.attrs['State']['FinishedAt']
    }
