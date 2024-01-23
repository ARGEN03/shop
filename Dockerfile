# # FROM python:3.11-slim

# # ENV PYTHONIOENCODING UTF-8
# # ENV TZ = Asia/Bishkek

# # WORKDIR /app
# # COPY . /app/

# # RUN pip install -r requirements.txt

# # CMD python3 manage.py migrate \
# #     && python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='argen.arzykulov03@gmail.com').exists() or User.objects.create_superuser('argen.arzykulov03@gmail.com', 'argen')" \
# #     && python3 manage.py runserver 0.0.0.0:80

# FROM python:3

# ENV PYTHONIOENCODING UTF-8
# ENV TZ=Asia/Bishkek

# # RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# RUN mkdir static && mkdir media
# COPY . .

# RUN python3 manage.py collectstatic --noinput

# EXPOSE 8000

FROM python:3

ENV PYTHONIOENCODING UTF-8
ENV TZ = Asia/Bishkek


# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir static && mkdir media 
COPY . .

RUN python3 manage.py collectstatic --noinput

EXPOSE 8000