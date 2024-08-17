import subprocess
import os
# Définissez les chemins appropriés
knime_executable = os.getenv('KNIME_PATH')
workflow_dir = r"recommender-system-workflow\movie_recommenders"

# Construire la commande à exécuter
cmd = [
    knime_executable,
    '-consoleLog',
    '-nosplash',
    '-application', 'org.knime.product.KNIME_BATCH_APPLICATION',
    '-workflowDir=' + workflow_dir,
    '-reset'
]

# Exécution de la commande
try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print("Workflow exécuté avec succès")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Erreur lors de l'exécution du workflow")
    print(e.stdout)
    print(e.stderr)