from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Field,Schema

app = Flask(__name__)
from graphene import ObjectType, String, Field

class Person(ObjectType):
    full_name = String()

    def resolve_full_name(parent, info):
        return f"{parent.first_name} {parent.last_name}"

class Query(ObjectType):
    me = Field(Person)

    def resolve_me(parent, info):
        # returns an object that represents a Person
        return Person("Kusumakar")

schema = Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))


if __name__ == '__main__':
    app.run()