import facebook

def main():
  # Page id and access token
  cfg = {
    "page_id"      : "564302177092977",  
    "access_token" : "EAAGIj6QJs3oBAC2VEy6mPwokpz9oyaQwSxvZAl9YyZA0qjjZALH0LyaPBiU9EdxfvZAj62gyykoLWa8Rc5lHbAPNZChjBg5Fsjj3i4A57DGfpe9gzZChpGeLCAAYUxTkZCMZAP8tC1ZBS0Gj9faFFPsVj5aqPmVIjkZAoZD"   # Step 3
    }

  api = get_api(cfg)
  msg = "Your message :)"
  status = api.put_wall_post(msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])

  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  

if __name__ == "__main__":
  main()