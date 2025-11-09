CREATE TABLE produtos(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    recorrencia VARCHAR(50) NOT NULL,
    disponivel BOOLEAN NOT NULL DEFAULT TRUE
)

INSERT INTO produtos (id, codigo_produto, nome, descricao, preco, tipo, recorrencia, disponivel) VALUES
(1, 'FIT-BIO-001', 'Fitmass Bioscan', 'Balança de bioimpedância com tela de x polegadas.', 8599.00, 'Hardware', 'Pagamento único', TRUE),
(2, 'FIT-POC-001', 'Fitmass Pocket', 'App de gestão de alunos para personal trainers (até 100 alunos) ou nutricionistas.', 49.90, 'Software', 'Mensal', TRUE),
