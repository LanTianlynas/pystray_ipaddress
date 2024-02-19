from main import db
from main.model.symbol_data_model import SymbolData
from main.model.symbol_model import Symbol
from main.model.exchange_model import Exchange
from main.model.node_model import Node


class SQLBuild:
    @classmethod
    def get_all_nodes(cls):
        all_symbols = Symbol.query.all()
        all_nodes = Node.query.all()

        symbol_list = []

        for node in all_nodes:
            count = 0
            for symbol in all_symbols:
                if node.code in symbol.node:
                    symbol_list.append(symbol)
                    count += 1
                if count == 5:
                    break

        return symbol_list

    @classmethod
    def delete_symbols(cls):
        all_symbols = Symbol.query.all()
        count = Symbol.query.count()
        print(count)
        keep_list = cls.get_all_nodes()
        print(len(keep_list))
        for symbol in all_symbols:
            if symbol not in keep_list:
                _symbol = Symbol.query.get(symbol.id)
                db.session.delete(_symbol)
                db.session.commit()

    @classmethod
    def delete_symbol_data(cls):
        all_symbol_data = SymbolData.query.all()
        for symbol_data in all_symbol_data:
            _symbol_data = SymbolData.query.get(symbol_data.id)
            db.session.delete(_symbol_data)
            db.session.commit()





