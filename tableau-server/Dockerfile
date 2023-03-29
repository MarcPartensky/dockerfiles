FROM fedora

RUN dnf update -y
RUN wget https://downloads.tableau.com/drivers/linux/yum/tableau-driver/tableau-postgresql-odbc-09.06.0500-1.x86_64.rpm
RUN dnf install -y tableau-postgresql-odbc-09.06.0500-1.x86_64.rpm
