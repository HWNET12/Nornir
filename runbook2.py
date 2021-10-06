from nornir import init_nornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = init_nornir.InitNornir(config_file="config.yaml")

def random_config(task):
    task.run(task=send_config, config=f"no ntp server {task.host['ntp_server']}")
    
results = nr.run(task=random_config)

print_result(results)
    