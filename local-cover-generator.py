import svgwrite
from pathlib import Path
import frontmatter
import re

def create_cover_image(title, output_path, blog_name="ByteForge"):
    # SVG canvas
    dwg = svgwrite.Drawing(str(output_path), size=(1200, 630))
    
    # Background gradient
    dwg.add(dwg.rect(insert=(0,0), size=('100%', '100%'), fill='url(#grad)'))
    
    # Gradient definition
    gradient = dwg.defs.add(dwg.linearGradient(id='grad', x1='0%', y1='0%', x2='100%', y2='100%'))
    gradient.add_stop_color(offset='0%', color='#1e1b4b')
    gradient.add_stop_color(offset='100%', color='#312e81')
    
    # Main title (multiline handling)
    title_lines = [title[i:i+40] for i in range(0, len(title), 40)]
    y_position = 280
    
    for line in title_lines[:3]:
        title_elem = dwg.text(line, insert=(600, y_position), 
                              text_anchor="middle", font_size="42", 
                              fill="white", font_family="Arial, sans-serif", 
                              font_weight="bold")
        dwg.add(title_elem)
        y_position += 60
    
    # Blog name at bottom
    brand = dwg.text(blog_name, insert=(600, 550), 
                     text_anchor="middle", font_size="28", 
                     fill="#a5b4fc", font_family="Arial")
    dwg.add(brand)
    
    dwg.save()
    return True

def process_all_posts():
    blog_dir = Path("src/content/blog")
    images_dir = Path("public/assets/posts")
    images_dir.mkdir(parents=True, exist_ok=True)
    
    for md_file in blog_dir.glob("*.md"):
        try:
            print(f"Processing: {md_file.name}")
            post = frontmatter.load(md_file)
            title = post.get('title', md_file.stem)
            
            image_filename = f"{md_file.stem}-cover.svg"
            image_path = images_dir / image_filename
            
            if image_path.exists():
                print(f"  ⏭️  Image already exists: {image_filename}")
                continue
                
            print(f"  🎨 Creating cover for: {title[:50]}...")
            if create_cover_image(title, str(image_path)):
                post['image'] = f"/assets/posts/{image_filename}"
                # Fix: Open file in text mode instead of binary mode
                with open(md_file, 'w', encoding='utf-8') as f:
                    frontmatter.dump(post, f)
                print(f"  ✅ Saved: {image_filename}")
            else:
                print(f"  ❌ Failed to create image")
        except Exception as e:
            print(f"  ❌ Error processing {md_file.name}: {e}")
    
    print("\n🎉 All done!")

if __name__ == "__main__":
    process_all_posts()
