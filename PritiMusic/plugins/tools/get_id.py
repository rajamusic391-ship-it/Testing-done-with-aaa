from pyrogram import filters
from PritiMusic import app

@app.on_message((filters.forwarded | filters.command("getid")) & ~filters.bot)
async def get_emoji_ids(client, message):
    msg = message.reply_to_message if message.reply_to_message else message
    emoji_ids = []

    # Entities check (Emojis in text/caption)
    entities = msg.entities or msg.caption_entities
    if entities:
        for ent in entities:
            if ent.custom_emoji_id:
                emoji_ids.append(ent.custom_emoji_id)

    # Sticker check
    if msg.sticker and msg.sticker.custom_emoji_id:
        emoji_ids.append(msg.sticker.custom_emoji_id)

    if emoji_ids:
        # Duplicate hatane ke liye
        unique_ids = list(dict.fromkeys(emoji_ids))
        
        result = ""
        for i, eid in enumerate(unique_ids, 1):
            result += f"**{i}.** ID: `{eid}`\n"
            
        await message.reply_text(
            f"**✅ Found Custom Emoji IDs:**\n\n{result}\n"
            "__Note: Bot cannot show emojis here due to Telegram restrictions. "
            "Match the numbers (1, 2, 3...) with the order of emojis in your forwarded message.__"
        )
    else:
        if message.command:
            await message.reply_text("Bhai, is message mein koi premium emoji nahi mila.")
