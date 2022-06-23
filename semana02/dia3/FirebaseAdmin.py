
class FirebaseAdmin:

    def __init__(self,db):
        self.db = db

    def getCollection(self,collectionName):
        lstCollection = []
        collectionValues = self.db.collection(collectionName)
        docValues = collectionValues.get()
        for doc in docValues:
            dicCollection = doc.to_dict()
            lstCollection.append(dicCollection)
        
        return lstCollection
