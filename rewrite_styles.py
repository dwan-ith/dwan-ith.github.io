css = '''
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}
.card {
  background: #f1f3f4;
  border-radius: 8px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.card-meta {
  font-size: 0.8rem;
  color: #666;
  text-transform: uppercase;
  margin-bottom: 0.5rem;
}
.card-title {
  font-size: 1.1rem;
  font-weight: 500;
  margin: 0 0 0.5rem 0;
  color: #111;
}
.card-desc {
  font-size: 0.95em;
  color: #555;
  margin: 0;
  line-height: 1.4;
}
'''
with open('styles.css', 'a') as f:
    f.write(css)

