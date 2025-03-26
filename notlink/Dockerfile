# Étape de clonage
FROM alpine:3.18 as cloner
RUN apk add --no-cache git
RUN git clone https://github.com/abdibrokhim/notlink /app

# Étape de construction
FROM rust:1.72-alpine as builder

# Installer les dépendances de build
RUN apk add --no-cache musl-dev openssl-dev

WORKDIR /app

# Copier les fichiers Cargo en premier pour le cache
COPY --from=cloner /app/Cargo.toml /app/Cargo.lock ./

# Créer un source dummy pour le cache des dépendances
RUN mkdir src && echo "fn main() {}" > src/main.rs

# Build des dépendances
RUN cargo build --release

# Copier le vrai code source
COPY --from=cloner /app .

# Forcer la recompilation du code source
RUN touch src/main.rs

# Build final
RUN cargo build --release --frozen

# Étape d'exécution
FROM alpine:3.18

WORKDIR /app

# Dépendances runtime
RUN apk add --no-cache openssl ca-certificates

# Copier le binaire
COPY --from=builder /app/target/release/notlink .

EXPOSE 8080

CMD ["./notlink"]
