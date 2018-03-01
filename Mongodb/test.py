import pymongo
import time 

client = pymongo.MongoClient('localhost', 27017);
db = client['zhihu'];   # 类似dict，若不存在，则新建；
# client.drop_database('zhihu') # 删除db

collection = db['zhihu'];   # 若不存在，则新建；
# db.drop_collection('zhihu') # 删除collection

document_test = {'name': 'test', 'time': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}
test_id = collection.insert(document_test);
# collection.find_one({'name': 'test'})
# collection.find({'name': 'test'}) 返回curser，可继续进行find,count等操作
# collection.update({'name': 'test'}, {'$set': {'name': 'test_update'}})
print(test_id)

