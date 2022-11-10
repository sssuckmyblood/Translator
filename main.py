import main_ui
import sqlite


def translate_action(text, origin, dest):
    db = sqlite.connect_db()
    check = db.cursor()
    check.execute("select * from ru;")
    for row in check.fetchall():
        print(row)
    check.close()
    if origin == "ru":
        try:
            check = db.cursor()
            check.execute("select dest_text from ru where origin_text = :text and dest_lan = :dest;",
                          {"text": text,
                           "dest": dest
                           })
            query_result = check.fetchone()
            check.close()
            if query_result is None:
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(text, src=origin, dest=dest).text
                insert = db.cursor()
                insert.execute("insert into ru ("
                               "origin_text, "
                               "dest_lan,"
                               "dest_text) values ("
                               "                    :origin, "
                               "                    :dest, "
                               "                    :result)",
                               {"origin": text,
                                "dest": dest,
                                "result": result
                                })
                db.commit()
                insert.close()
                return result
            else:
                return query_result[0]

        except db.Error as error:
            print("Ошибка чтения кэша", error)

        finally:
            if db:
                db.close()
    elif dest == "ru":
        try:
            check = db.cursor()
            check.execute("select origin_text from ru where dest_text = :text and dest_lan = :origin;",
                          {"text": text,
                           "origin": origin
                           })
            query_result = check.fetchone()
            check.close()
            if query_result is None:
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(text, src=origin, dest=dest).text
                insert = db.cursor()
                insert.execute("insert into ru ("
                               "origin_text, "
                               "dest_lan,"
                               "dest_text) values ("
                               "                    :result, "
                               "                    :dest, "
                               "                    :origin)",
                               {"result": result,
                                "dest": origin,
                                "origin": text
                                })
                db.commit()
                insert.close()
                return result
            else:
                return query_result[0]

        except db.Error as error:
            print("Ошибка чтения кэша", error)

        finally:
            if db:
                db.close()
    elif origin == "be":
        try:
            check = db.cursor()
            check.execute("select dest_text from be where origin_text = :text and dest_lan = :dest;",
                          {"text": text,
                           "dest": dest
                           })
            query_result = check.fetchone()
            check.close()
            if query_result is None:
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(text, src=origin, dest=dest).text
                insert = db.cursor()
                insert.execute("insert into be ("
                               "origin_text, "
                               "dest_lan,"
                               "dest_text) values ("
                               "                    :origin, "
                               "                    :dest, "
                               "                    :result)",
                               {"origin": text,
                                "dest": dest,
                                "result": result
                                })
                db.commit()
                insert.close()
                return result
            else:
                return query_result[0]

        except db.Error as error:
            print("Ошибка чтения кэша", error)

        finally:
            if db:
                db.close()
