import requests
from gql import Client, gql
import os

hashnode_url = "https://gql.hashnode.com"
# The headers variable is used to store the authentication token and alert the API of the format data will be sent.

api_auth_key = os.environ.get('HASHNODE_API_KEY')
if api_auth_key is not None:
    
    auth_headers = {"Authorization": f"{api_auth_key}"}

else:
    print("Error: HASHNODE_API_KEY is not set.")
 
#Graphql Mutation for publishing a new post
post_mutation = """
    PublishPost($input: PublishPostInput!) {
        publishPost(input: $input) {
    post {
      id
      slug
      title
      subtitle
      author {
        ...UserFragment
      }
      coAuthors {
        ...UserFragment
      }
      tags {
        ...TagFragment
      }
      url
      canonicalUrl
      publication {
        ...PublicationFragment
      }
      cuid
      coverImage {
        ...PostCoverImageFragment
      }
      brief
      readTimeInMinutes
      views
      series {
        ...SeriesFragment
      }
      reactionCount
      replyCount
      responseCount
      featured
      contributors {
        ...UserFragment
      }
      commenters {
        ...PostCommenterConnectionFragment
      }
      comments {
        ...PostCommentConnectionFragment
      }
      bookmarked
      content {
        ...ContentFragment
      }
      likedBy {
        ...PostLikerConnectionFragment
      }
      featuredAt
      publishedAt
      updatedAt
      preferences {
        ...PostPreferencesFragment
      }
      audioUrls {
        ...AudioUrlsFragment
      }
      seo {
        ...SEOFragment
      }
      ogMetaData {
        ...OpenGraphMetaDataFragment
      }
      hasLatexInPost
      isFollowed
      isAutoPublishedFromRSS
      features {
        ...PostFeaturesFragment
      }
    }
  }
}
"""
# The input variables for the query
PublishPostInput = {
    "user_id" : 'id',
    "slug" : 'slug',
    "title" : 'Blog Title',
    "subtitle" : 'Blog Subtitle',
    "author" : "Author"
}

# Variables for the Graphql Mutation
input_variables = {"input": PublishPostInput}

#Graphql Payload
request_payload = {
    "query": post_mutation,
    "variables" : input_variables
}

# Graphql Request
def make_graphql_request(url, headers, json):
  response = requests.post(url=hashnode_url, headers=auth_headers, json=request_payload)

  if response.status_code == 200:
    print("Blog posted successfully!")
  else:
    print("An error occurred. Kindly check on it and try again!")

  return response
