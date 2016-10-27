############################################################
# Dockerfile to build apache-flask container images
# Based on Ubuntu
############################################################

# Set the base image to the operation zombie base image
FROM operationzombie/base

# File Author / Maintainer
MAINTAINER Layne Small

# Create the default directory
RUN mkdir -p /srv/www
RUN mkdir -p /srv/scripts

ADD image_scripts/ /srv/scripts

# Clone the app from github and install packages
RUN git clone https://github.com/callumgill/apache-flask.git /srv/www/app #8
RUN cp -f /srv/www/app/apache/config/default.conf /etc/apache2/sites-available/000-default.conf
RUN cp -f /srv/scripts/serial_port_listener /etc/init.d/serial_port_listener
RUN ln -s /etc/init.d/serial_port_listener /etc/rc5.d/S03serial_port_listener
RUN pip install -r /srv/www/app/requirements.txt
RUN /etc/init.d/serial_port_listener start

##################### INSTALLATION END #####################

# Expose the default port
EXPOSE 80
EXPOSE 8082
EXPOSE 8083

# Set default container command
ENTRYPOINT /usr/sbin/apache2ctl -D FOREGROUND
