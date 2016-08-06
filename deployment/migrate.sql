ALTER TABLE auth_user ADD CONSTRAINT unique__auth_user__id UNIQUE (id);
ALTER TABLE django_site ADD CONSTRAINT unique__django_site__id UNIQUE (id);
