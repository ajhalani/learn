Types::PostType = GraphQL::ObjectType.define do
  name "Post"
  field :title, types.String
  field :rating, types.Int
  field :comments, types[Types::CommentType]
end

Types::CommentType = GraphQL::ObjectType.define do
  name "Comment"
  field :id, !types.ID
  field :body, !types.String
  field :created_at, !types.String
end

