FROM arm64v8/ruby:3.3

WORKDIR /srv/jekyll

RUN gem install bundler

# Copy Gemfile and Gemfile.lock
COPY Gemfile* ./

# Install dependencies
RUN bundle install


# RUN jekyll build --destination /srv/jekyll/_site


CMD ["jekyll", "serve", "--verbose", "--host", "0.0.0.0"]
