#!/usr/bin/python
import psycopg2
from data_saver_program.config import config


class data_saver():

    def __init__(self):
        commands = (
            #
            #    legal_representative text,
            #   person_in_charge_of_enterprise text,
            #  residence_address text,
            # business_address text,
            # business_mode text,
            # storage_address text,
            # issue_department text,
            """
            CREATE TABLE IF NOT EXISTS public.company (
                registered_id text,
                company_name text,
                business_scope text,
                issue_date text,
                exp text
            )
            """
        )
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            print("Connecting...")
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # display the PostgreSQL database server version
            print('PostgreSQL database version: ', end='')
            cur.execute('SELECT version()')
            db_version = cur.fetchone()
            print(db_version)
            print("Connection established")
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("Failed!")
        finally:
            if conn is not None:
                conn.close()
        self.run_query(commands, ())

    def run_query(self, query, tpl):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(query, tpl)
            cur.close()
            conn.commit()
            # print("Completed!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
            # print("Connection closed")

    def copy_data_from_csv(self):
        self.run_query(
            "COPY public.medical_equipment FROM 'D:\demo\Result_copy.csv' delimiter ',' csv header", ())

    def insert_data(self, info):
        self.run_query(
            "INSERT INTO public.company VALUES (%s,%s,%s,%s,%s);", (info[0], info[1], info[7],
                                                                    info[10], info[11]))
