from app import db, ma
from datetime import datetime
from marshmallow import fields


class Publishers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

    @classmethod
    def select_or_create(cls, username):
        publisher = Publishers.query.filter_by(username=username).first()

        if publisher:
            return publisher

        new_publisher = Publishers(username=username)
        db.session.add(new_publisher)
        db.session.commit()

        return new_publisher


class Advertisements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
    publisher = db.relationship("Publishers", backref="advertisements")

    @classmethod
    def delete(cls, advertisement):
        db.session.delete(advertisement)
        db.session.commit()

        return advertisement


class PublisherSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('id', 'username')
        ordered = True


class AdvertisementSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('id', 'title', 'description', 'created_on', 'publisher')
        ordered = True

    publisher = ma.Nested(PublisherSchema)
    title = fields.String(required=True)
    description = fields.String(required=True)


advertisement_schema = AdvertisementSchema()
all_advertisements_schema = AdvertisementSchema(many=True)

db.create_all()
