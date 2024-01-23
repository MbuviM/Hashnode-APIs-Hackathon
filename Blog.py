import requests
from gql import Client, gql



def publish_blog(PublishPostInput, Hashnode_API_key):
    url = "https://gql.hashnode.com"
    Hashnode_API_key = "PAT"

    #Graphql Mutation for publishing a new post
    
    mutation = """
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


