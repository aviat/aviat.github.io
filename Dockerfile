FROM arm64v8/ruby:3.3

WORKDIR /srv/jekyll

RUN gem install bundler

# Copy Gemfile and Gemfile.lock
COPY Gemfile* /srv/jekyll/

RUN ls /srv/jekyll

# Install dependencies
RUN cd /srv/jekyll && bundle install

CMD ["bundle", "exec", "jekyll", "serve", "--verbose", "--host", "0.0.0.0"]
