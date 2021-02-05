from setuptools import setup, find_packages

requirements = []
with open('requirements.txt.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            requirements.append(line)

setup(
    name='mqtt_utils',
    version='0.2.0',
    description='Library making connection to mqtt broker, '
                'receiving and sending messages',
    author='Karol Misiarz',
    author_email='forkarolm@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7'
)
