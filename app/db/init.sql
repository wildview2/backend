CREATE TABLE if not exists rookeries (
id SERIAL PRIMARY KEY,
latitude float8,
longitude float8,
name text not null
);

CREATE TABLE if not exists results  (
  dat timestamp,
  valruses_number integer,
  photo text,
  rookery_id integer references rookeries(id) on delete cascade
);
