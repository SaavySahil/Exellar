    def to_dict(self, full=False):
        data = {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'category': self.category,
            'status': self.status,
            'location': self.location,
            'scope': self.scope,
            'size': self.size,
            'client_name': self.client_name,
            'thumbnail': self.thumbnail,
            'is_featured': self.is_featured,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
        if full:
            data.update({
                'services': self.services,
                'partners': self.partners,
                'story_headline': self.story_headline,
                'story_body': self.story_body,
                'client_testimonial': self.client_testimonial,
                'gallery': self.get_gallery(),
            })
        return data
