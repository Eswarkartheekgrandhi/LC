from config.mongoConfig import getMongoConnection


def insertData(data, collectionName, dbName):
    conn, collection = getMongoConnection(dbName, collectionName)
    collection.insert_one(data)
    conn.close()


def getData(identifier, collectionName, dbName):
    conn, collection = getMongoConnection(dbName, collectionName)
    data = list(collection.find(identifier))
    conn.close()
    return data


def updateData( identifier, updateQuery, collectionName, dbName):
    conn, collection = getMongoConnection(dbName, collectionName)
    collection.update_one(identifier, updateQuery)
    conn.close()