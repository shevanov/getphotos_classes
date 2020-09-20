INSERT INTO photos VALUES (
                        %(album_id)s,
                        %(date)s,
                        %(id)s,
                        %(owner_id)s,
                        %(image)s
                        ) ON CONFLICT DO NOTHING;