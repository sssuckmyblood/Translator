'''
Модуль работы с переводом слов через google api и их записи в базу данных
'''


import sqlite


def translate_action(text, origin, dest):
    db = sqlite.connect_db()
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
                result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
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
                result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
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
                    result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
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


            finally:
                if db:
                    db.close()

    elif dest == "be":
        try:
            check = db.cursor()
            check.execute("select origin_text from be where dest_text = :text and dest_lan = :origin;",
                          {"text": text,
                           "origin": origin
                           })
            query_result = check.fetchone()
            check.close()
            if query_result is None:
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
                insert = db.cursor()
                insert.execute("insert into be ("
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


        finally:
            if db:
                db.close()

    elif origin == "uk":
            try:
                check = db.cursor()
                check.execute("select dest_text from uk where origin_text = :text and dest_lan = :dest;",
                              {"text": text,
                               "dest": dest
                               })
                query_result = check.fetchone()
                check.close()
                if query_result is None:
                    from googletrans import Translator
                    translator = Translator()
                    result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
                    insert = db.cursor()
                    insert.execute("insert into uk ("
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


            finally:
                if db:
                    db.close()

    elif dest == "uk":
        try:
            check = db.cursor()
            check.execute("select origin_text from uk where dest_text = :text and dest_lan = :origin;",
                          {"text": text,
                           "origin": origin
                           })
            query_result = check.fetchone()
            check.close()
            if query_result is None:
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
                insert = db.cursor()
                insert.execute("insert into uk ("
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

        finally:
            if db:
                db.close()

    elif origin == "en":
            try:
                check = db.cursor()
                check.execute("select dest_text from en where origin_text = :text and dest_lan = :dest;",
                              {"text": text,
                               "dest": dest
                               })
                query_result = check.fetchone()
                check.close()
                if query_result is None:
                    from googletrans import Translator
                    translator = Translator()
                    result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
                    insert = db.cursor()
                    insert.execute("insert into en ("
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


            finally:
                if db:
                    db.close()

    elif dest == "en":
        try:
            check = db.cursor()
            check.execute("select origin_text from en where dest_text = :text and dest_lan = :origin;",
                          {"text": text,
                           "origin": origin
                           })
            query_result = check.fetchone()
            check.close()
            if query_result is None:
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
                insert = db.cursor()
                insert.execute("insert into en ("
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


        finally:
            if db:
                db.close()

    elif origin == "de":
            try:
                check = db.cursor()
                check.execute("select dest_text from de where origin_text = :text and dest_lan = :dest;",
                              {"text": text,
                               "dest": dest
                               })
                query_result = check.fetchone()
                check.close()
                if query_result is None:
                    from googletrans import Translator
                    translator = Translator()
                    result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
                    insert = db.cursor()
                    insert.execute("insert into de ("
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


            finally:
                if db:
                    db.close()

    elif dest == "de":
        try:
            check = db.cursor()
            check.execute("select origin_text from de where dest_text = :text and dest_lan = :origin;",
                          {"text": text,
                           "origin": origin
                           })
            query_result = check.fetchone()
            check.close()
            if query_result is None:
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
                insert = db.cursor()
                insert.execute("insert into de ("
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


        finally:
            if db:
                db.close()

    elif origin == "fr":
            try:
                check = db.cursor()
                check.execute("select dest_text from fr where origin_text = :text and dest_lan = :dest;",
                              {"text": text,
                               "dest": dest
                               })
                query_result = check.fetchone()
                check.close()
                if query_result is None:
                    from googletrans import Translator
                    translator = Translator()
                    result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
                    insert = db.cursor()
                    insert.execute("insert into fr ("
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

            finally:
                if db:
                    db.close()

    elif dest == "fr":
        try:
            check = db.cursor()
            check.execute("select origin_text from fr where dest_text = :text and dest_lan = :origin;",
                          {"text": text,
                           "origin": origin
                           })
            query_result = check.fetchone()
            check.close()
            if query_result is None:
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(text, src=origin, dest=dest).text.lower().strip()
                insert = db.cursor()
                insert.execute("insert into fr ("
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


        finally:
            if db:
                db.close()

def get_word_list():
    db = sqlite.connect_db()
    data = db.cursor()
    data.execute("select origin_text from ru;")
    result = data.fetchall()
    data.close()
    return result


def get_translation(origin):
    db = sqlite.connect_db()
    data = db.cursor()
    data.execute("select dest_lan, dest_text from ru where origin_text = :origin;",
                 { "origin": origin})
    result = data.fetchall()
    data.close()
    return result

