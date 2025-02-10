# Pull the official odoo image
FROM odoo:16.0
# Install additional requirements
USER root
COPY --chown=odoo:odoo ./requirements.txt /mnt/requirements_extra.txt
RUN pip3 install --upgrade pip setuptools \
    && pip3 install --default-timeout=100 -r /mnt/requirements_extra.txt
USER odoo